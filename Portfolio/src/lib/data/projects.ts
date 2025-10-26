export const PROJECTS = [
  {
    name: "PolicyScope",
    desc: "LLM-assisted document analyzer for audits/policies. Chunking + RAG + evaluators; exports insights.",
    tags: ["TypeScript", "React", "Azure OpenAI", "RAG"],
    details: `
A compact RAG system with chunking, retrieval evaluators, and exportable insights.
- Frontend: React + TypeScript with clean, accessible UI
- Backend: Azure OpenAI + vector search
- Notes: Emphasis on reliability and small evaluation loops
`.trim(),
  },
  {
    name: "NetDiag",
    desc: "Diagnostics toolkit that monitors cloud connectivity and deployment health with alerts and dashboards.",
    tags: ["C#", ".NET", "Azure"],
    details: `
Probes cloud endpoints, measures latency, and surfaces health checks.
- Backend: .NET Web API
- Dashboards: time-series metrics and alerts
- Result: Faster incident triage and fewer false alarms
`.trim(),
  },
  {
    name: "CineUX",
    desc: "Experimental player controls & accessibility overlays for a streaming app prototype.",
    tags: ["React Native", "TypeScript"],
    details: `
Explored player UX and accessibility features with custom overlays.
- Tech: React Native + TypeScript
- Perf: Optimized re-render paths
- Outcome: Smoother controls and better a11y affordances
`.trim(),
  },
]
