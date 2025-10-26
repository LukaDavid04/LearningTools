export const JOURNAL = [
  {
    slug: "reliable-ai-features",
    title: "On writing reliable AI features",
    date: "2025-09-15",
    tags: ["LLM", "Evaluation", "RAG"],
    excerpt: "Notes on guardrails, small evals that catch big issues, and pragmatic ways to ship safely.",
    content: `
Building reliable AI features starts with simple checks that catch common failure modes.
Keep the loops small, log decisions, and evaluate retrieval quality automatically.
    `.trim(),
  },
  {
    slug: "good-engineering-handoff",
    title: "What makes a good engineering handoff",
    date: "2025-07-02",
    tags: ["Process", "Collaboration"],
    excerpt: "Checklists, traceability, and reducing surprise for the next person in line.",
    content: `
A good handoff minimizes surprise. I keep a one-pager with context, current state,
open questions, and test notes. Leave breadcrumbs and make the next step obvious.
    `.trim(),
  },
  {
    slug: "tennis-flow-debugging",
    title: "Tennis, flow, and debugging",
    date: "2024-11-11",
    tags: ["Mindset"],
    excerpt: "Finding rhythm in practice and in code. A few parallels that help me focus.",
    content: `
When I coach or play tennis, rhythm matters. In debugging, the same applies.
Warm up with a trivial repro. Hit a few simple shots. Then increase complexity.
    `.trim(),
  },
] as const;

export type JournalEntryType = typeof JOURNAL[number];
