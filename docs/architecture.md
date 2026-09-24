# Proposed lab architecture

Status: **DESIGN ONLY — REQUIRES MANUAL EXECUTION**. No hypervisor, VM, interface, firewall rule, collection pipeline, or detection has been validated. The [README diagram](../README.md#arquitectura) is the canonical Mermaid topology.

## Design goals and constraints

Use a small isolated environment to reconstruct security events across endpoint, identity, and network sources. Wazuh remains the primary SIEM; Splunk is introduced only after the Wazuh investigations work. Build incrementally so limited hardware does not require every VM to run at once.

The local repository was created on an x86_64 macOS host. Available memory, storage, hypervisor support, guest licensing, and VM access have not been established. Choose a supported hypervisor and current compatible guest/tool versions in Deliverable 1; record versions and official download sources then. No installation commands or deployment configurations are provided in Deliverable 0.

## Host inventory and sizing

All hostnames and addresses below are proposed lab identifiers, not observed assets. Verify the subnet does not overlap a home network, VPN, or other virtual network before assigning it.

| Name | IPv4 | Role | Initial planning budget (vCPU / RAM / disk) | First phase |
| --- | --- | --- | --- | --- |
| SOC-WAZUH | 10.10.10.10 | Wazuh server, indexer, dashboard on one supported Linux VM | 4 / 8 GiB / 80 GB | 1 |
| SOC-DC01 | 10.10.10.20 | Windows Server 2025 evaluation, AD DS, DNS | 2 / 4 GiB / 64 GB | 7 |
| SOC-WIN11 | 10.10.10.30 | Windows 11 Enterprise evaluation, Wazuh agent, Sysmon, Defender | 2 / 4 GiB / 80 GB | 1 |
| SOC-LINUX | 10.10.10.40 | Ubuntu Server, OpenSSH, Wazuh agent, audit; later Suricata | 2 / 4 GiB / 40 GB | 2; sensor in 6 |
| SOC-SIM | 10.10.10.50 | Separate bounded event-generation VM | 2 / 2 GiB / 30 GB | 3 |
| Host management adapter | 10.10.10.1 (reserved) | Analyst-to-lab management only; never a simulation target | Host resources | 1 |

These are budgeting assumptions, not verified performance or minimum requirements. Wazuh's current quickstart recommends 4 vCPU, 8 GiB RAM, and 50 GB for 1–25 agents; the proposed 80 GB adds room for this lab, but retention still depends on event volume. [Wazuh quickstart](https://documentation.wazuh.com/current/quickstart.html).

The five guest budgets total 22 GiB RAM and 294 GB virtual disk capacity, before host overhead, installation media, and snapshots. Deliverable 1 starts with 12 GiB guest RAM and 160 GB virtual disk capacity. Do not assume thin provisioning or CPU overcommit makes all guests practical on the current host. Reduce concurrent phases or use another owned host if capacity is inadequate; do not silently remove required telemetry to fit.

## Network boundaries and visibility

Use a host-only virtual switch for `10.10.10.0/24`, with static addresses, no guest default gateway during simulations, and no host IP forwarding/Internet sharing. The analyst host remains reachable on that switch for management; it is outside the target allowlist. A private address alone does not establish isolation.

Before each simulation, verify guest adapters, IPv4/IPv6 routes, host forwarding, VPN routes, and firewall exposure. No bridged adapter, public port forwarding, or routed path to a home/company network is allowed. Inspect configuration and routing without sending probes to public systems. Use a console if host-only management is unavailable; document the changed access path.

Temporary outbound NAT may be attached for official updates and package installation. Record when it is enabled; remove or disconnect it before testing. Do not run simulations while guests are dual-homed. Keep Defender enabled. Take snapshots before state-changing tests and record cleanup and recovery steps.

### Initial sensor placement

Suricata will capture on SOC-LINUX's lab interface. SOC-005 scans SOC-LINUX from SOC-SIM; SOC-006 sends a harmless Windows request to a local service on SOC-LINUX. This places the tested traffic on the sensor's actual interface. Suricata cannot be assumed to see unicast traffic between other VMs merely because they share a virtual switch.

If later scenarios need other east-west traffic, explicitly configure and validate virtual-switch mirroring or a dedicated capture path first. Validate with a known lab flow and packet/event counts. DNS traffic from Windows to the domain controller requires endpoint DNS events, DNS server logging, or a capture on that path; the initial Ubuntu sensor does not cover it. Packet capture inspection stays private by default.

Suricata EVE JSON can carry alerts and protocol/flow records, but output types and capture coverage must be configured and tested. An EVE flow is not automatically an IDS alert. [Suricata EVE documentation](https://docs.suricata.io/en/latest/output/eve/eve-json-output.html). That documentation's `latest` branch may describe development features; choose version-matched documentation before configuring the eventual stable installation.

### Intended flows

This table is a future firewall design input, not an applied rule set. Restrict sources and destinations explicitly; verify actual ports against chosen versions in their implementation phase.

| Source → destination | Intended service | Boundary |
| --- | --- | --- |
| Analyst host → Wazuh | HTTPS dashboard, typically TCP 443; SSH TCP 22 only if needed | Management only; never expose to Internet |
| Enrolled agents → Wazuh | Agent events, typically TCP 1514 | Owned lab agents only |
| New agents → Wazuh | Enrollment, typically TCP 1515 | Limit to enrollment period and named agents |
| Workstation → DC | DNS TCP/UDP 53 and required AD services | Define complete domain-join/service rules in phase 7 |
| Simulator → Ubuntu | SSH TCP 22; bounded approved scan ports | Exact per-test target list and attempt/port limits |
| Windows → Ubuntu | Temporary harmless HTTP service, proposed TCP 8080 | Scenario 006 only; stop service afterward |

Indexer/API back-end access stays internal to the all-in-one SIEM. Additional necessary flows, including AD time/Kerberos/LDAP/SMB/RPC and any remote administration, must be documented and verified before opening them. Avoid an unexplained allow-all rule as the final state.

## Identity, DNS, and time

Use the private test domain `soc.test` once SOC-DC01 exists. `.test` is reserved for testing; all required records must be hosted locally. Disable external forwarding during tests. [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606.html).

Deliverables 1–6 can operate as a workgroup; do not point clients at the nonexistent DC. Keep the lab adapter free of a public DNS dependency in the initial isolated stage. DNS investigation SOC-007 begins in phase 6 only if a local test resolver is configured; otherwise record the dependency and finish it after phase 7 supplies AD DNS.

Create only invented lab identities. Separate routine users, simulation accounts, and lab administrator accounts. Domain join, normal users, groups, and authorization records belong to phase 7. Never use workplace credentials.

Normalize report timestamps to UTC, retaining original timestamps/time zones and measured clock offsets. Use a verified guest/host time source initially and document domain time behavior once AD exists. Record drift before/after snapshots; snapshot restores can disrupt correlation. Do not assert event order within uncertainty caused by clock skew or ingestion delay.

## Telemetry contract

This is a collection plan, not a statement that events are available. Each source requires a known harmless source event, collection proof, ingestion proof, field verification, and documented gaps before its investigation starts.

| Source | Planned collection | Required investigative fields | Important qualification |
| --- | --- | --- | --- |
| Windows Security | Wazuh event-channel collection | Time, event ID, computer, actor/target user, logon type/result/status, source IP when present | Audit policy controls coverage; local logons may have no source IP |
| Windows System | Wazuh event-channel collection | Time, computer, provider, event ID, service/state | Establish health and service-change context |
| PowerShell Operational | Wazuh event-channel collection | Time, user/context, script block ID/content, host | Enable appropriate script-block/module logging; sensitive command content stays private |
| Sysmon Operational | Wazuh event-channel collection | ProcessGuid, process/parent image and command line, user, time, network tuple, DNS query/results | Explicitly configure needed event types and filters; correlate, do not assume every field appears in every event |
| Defender Operational | Wazuh event-channel collection | Time, computer, detection/action/configuration fields where applicable | Healthy configuration events do not prove malware detection |
| Linux SSH/auth/sudo | Agent reads verified journal or rsyslog-backed auth file | Time, host, user, source IP/port, result, service, sudo actor/target/command | Verify actual Ubuntu logging backend; avoid duplicate collection |
| Linux audit/process | Agent reads audit output after scoped audit setup | Time, audit ID, login UID/effective UID, executable, PID, arguments, result | Ordinary auth logs are insufficient for complete process/network attribution |
| Linux system/application | Agent reads selected journal/files | Time, host, service, action/error, local service request metadata | Document exact service and source paths when deployed |
| Wazuh FIM | Agent monitors a dedicated protected test path | Path, time, previous/current hash/state; actor if available | Actor attribution needs supported who-data/audit configuration; never infer actor solely from FIM |
| AD Security / DNS | DC agent and explicitly enabled DNS logging | Subject/target SID, account/group, logon result, client address, DNS answer when present | Distinguish DC authentication from workstation logon events; configure audit policy |
| Suricata EVE | Ubuntu agent reads selected JSON output | Time, source/destination IP/port, protocol, flow ID, DNS/HTTP/alert fields as available | Coverage limited to captured traffic; encrypted payload may be unavailable |
| CloudTrail / CloudWatch | Owner AWS account, selected reviewed exports in phase 10 | eventTime, eventName/source, userIdentity, sourceIPAddress, resources, request/response, error, eventID | Check trail/region/event coverage and CloudWatch delivery separately; no account access yet |

Sysmon provides process creation, network, and DNS events; network-connection logging is disabled by default. Deliverable 1 must record the chosen configuration and verify coverage. [Microsoft Sysmon documentation](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

An agent being connected does not prove all sources arrive. Wazuh alerts contain events that meet alerting rules; benign source events may need a deliberately enabled, temporary, bounded archive/indexing path for collection validation. Document which path was used and its retention; do not treat missing baseline events in the alerts index as proof the agent failed. No retention interval is validated yet.

## Separate and later environments

AWS work uses only the owner's dedicated lab account. IAM, CloudTrail, and CloudWatch setup, costs/retention, controlled change scope, access handling, and teardown belong to phase 10. The local test network does not gain Internet access for attack simulation. Only sanitized CloudTrail samples enter Git; no live credentials or public infrastructure targets are published.

Splunk is a later secondary analysis environment for sanitized datasets. Choose its host, version, resources, and index/source-type mapping in phase 11. Do not replace Wazuh or claim Enterprise Security use without actual access and evidence.

## Acceptance gates

- [ ] Host capacity, supported hypervisor/guest versions, and recovery method recorded.
- [ ] Lab network and exact target allowlist established; routes/adapters/forwarding verified.
- [ ] Versions, time sources, logging policies, and snapshots documented.
- [ ] Each required telemetry source verified end to end using a benign event.
- [ ] Sensor visibility demonstrated on each network investigation's actual path.
- [ ] Evidence sanitized and linked to reports; cleanup and detection gaps recorded.

These are future execution gates. See the [ordered implementation checklist](implementation-checklist.md).
