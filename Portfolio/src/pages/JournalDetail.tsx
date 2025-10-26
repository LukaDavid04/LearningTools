import { useParams, Link } from "react-router-dom";
import { JOURNAL } from "@/lib/data/journal";
import { ArrowLeft } from "lucide-react";

export function JournalDetail() {
  const { slug } = useParams<{ slug: string }>();
  const entry = JOURNAL.find((j) => j.slug === slug);

  if (!entry) {
    return (
      <div>
        <p className="text-sm text-muted-foreground">Entry not found.</p>
        <Link to="/journal" className="underline text-sm">Back to Journal</Link>
      </div>
    );
  }

  return (
    <article className="max-w-3xl">
      <Link to="/journal" className="inline-flex items-center gap-2 text-sm underline mb-4">
        <ArrowLeft className="h-4 w-4" /> Back to Journal
      </Link>

      <h1 className="text-3xl font-semibold tracking-tight">{entry.title}</h1>
      <div className="text-xs text-muted-foreground mt-1">{new Date(entry.date).toLocaleDateString()}</div>

      <div className="prose prose-sm sm:prose-base dark:prose-invert mt-6">
        {entry.content.split("\n\n").map((p, i) => (
          <p key={i} className="leading-7 whitespace-pre-wrap">{p}</p>
        ))}
      </div>
    </article>
  );
}
