---
name: engineering-networking
description: "Use when engineering work involves DNS, TCP/IP, TLS, ports, proxies, VPN, nginx, diagnostics. Provides senior baselines, traps, validation patterns, and focused references for this domain."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, networking]
    related_skills: [engineering-mastery, reasoning-mastery]
---

# Networking

## Mission

Handle DNS, TCP/IP, TLS, ports, proxies, VPN, nginx, diagnostics with senior discipline: frame first, inspect current context, implement/diagnose in small safe steps, verify with real evidence, and log reusable failures.

## When to Use

Use when the router selects this domain, or when the user's task directly mentions DNS, TCP/IP, TLS, ports, proxies, VPN, nginx, diagnostics.


## Operating Baseline
- Diagnose by layer: local link, IP, route, DNS, TCP port, TLS, HTTP, app.
- Use the right tool: ping, traceroute, dig, ss, curl, openssl, tcpdump/Wireshark.
- Distinguish name resolution, reachability, port binding, firewall, TLS, and app errors.
- Record commands and outputs.


## Workflow

1. Frame intent and success criteria.
2. Inspect existing system/docs/version.
3. Select smallest safe action.
4. Execute and verify.
5. Review security, correctness, maintainability, and failure modes.
6. Update `ERRORS.md` if a reusable issue appears.

## Common Pitfalls

See `references/baseline.md` for top traps and example patterns.

## Verification Checklist

- [ ] Problem framed.
- [ ] Current version/context checked.
- [ ] Failure cases considered.
- [ ] Runnable example/diagnosis verified.
- [ ] Result recorded in validation evidence when applicable.
