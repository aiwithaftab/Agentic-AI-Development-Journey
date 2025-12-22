Today i have learned about SRE (Site Reliability Engineering). In SRE, Agents represents a shift from traditional automation (Fixed Script) to Agentic System that can reson, plan, act and observe.

How SRE Agents Work
Unlike a standard script that follows a "If A, then B" logic, an SRE agent uses a reasoning loop. When an incident occurs, it follows a process similar to a human engineer:

Perceive: It ingests logs, metrics, and traces from observability tools (e.g., Datadog, Prometheus).

Reason: it forms a hypothesis (e.g., "Is this latency caused by the recent database migration?").

Act: It queries the infrastructure or runs a diagnostic tool to test that hypothesis.

Resolve: If empowered, it executes a fix (e.g., clearing a cache or scaling a pod) or presents a summarized finding to the human on-call.


