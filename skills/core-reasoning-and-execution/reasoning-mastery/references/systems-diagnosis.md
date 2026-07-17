# Systems and Diagnostic Thinking

See components, relationships, feedback loops, bottlenecks, second-order effects, and actual behavior. Debugging pattern: reproduce → isolate → hypothesize → test one variable → root cause → guard.

Primary sources/leads: Donella Meadows, Thinking in Systems and Leverage Points; Goldratt's Theory of Constraints; scientific debugging practice.

Procedure:
1. Reproduce the failure.
2. Draw path: input → process → output.
3. Identify where expected diverges from observed.
4. Binary search the system.
5. Test one variable at a time.
6. Fix root cause and add guard.

Worked example: “Telegram typing stuck” should not be patched at message text; diagnose gateway event loop, typing suppression, and client behavior.

Invoke this when: symptoms may mislead. This misleads when: you over-model instead of running a simple reproduction.
