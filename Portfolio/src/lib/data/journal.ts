export type JournalEntryComment = {
  paragraph: number;
  wordIndex: number;
  text: string;
};

export type JournalEntryType = {
  slug: string;
  title: string;
  date: string;
  tags: readonly string[];
  excerpt: string;
  content: string;
  comments?: readonly JournalEntryComment[];
};

export const JOURNAL: readonly JournalEntryType[] = [
  {
    slug: "reliable-ai-features",
    title: "Achieving a Dream Goal",
    date: "2025-10-11",
    tags: ["LLM", "Evaluation", "RAG"],
    excerpt:
      "What it meant to my team to make the finals of the Ontario University Athletics tennis tournament.",
    content: `
In first year, I used to get up at 5 am for practice. The cafeteria was closed, so I would bring a mug of cheerios with me as I waited in the freezing (literally) temperatures to get picked up by my best friend and club president Ryan.
    `.trim(),
    comments: [
      {
        paragraph: 0,
        wordIndex: 2,
        text: "I remember laughing about how cold those early mornings felt.",
      },
    ],
  },
  {
    slug: "good-engineering-handoff",
    title: "What makes a good engineering handoff",
    date: "2025-07-02",
    tags: ["Process", "Collaboration"],
    excerpt:
      "Checklists, traceability, and reducing surprise for the next person in line.",
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
    excerpt:
      "Finding rhythm in practice and in code. A few parallels that help me focus.",
    content: `
When I coach or play tennis, rhythm matters. In debugging, the same applies.
Warm up with a trivial repro. Hit a few simple shots. Then increase complexity.
    `.trim(),
  },
] as const;
