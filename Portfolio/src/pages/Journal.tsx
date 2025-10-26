import * as React from 'react'
import { Input } from '@/components/ui/input'
import { JOURNAL } from '@/lib/data/journal'
import { JournalEntry } from '@/components/journal-entry'

export function Journal() {
  const [q, setQ] = React.useState('')
  const filtered = React.useMemo(() => {
    const s = q.trim().toLowerCase()
    if (!s) return JOURNAL
    return JOURNAL.filter((j) => j.title.toLowerCase().includes(s) || j.excerpt.toLowerCase().includes(s) || j.tags.join(' ').toLowerCase().includes(s))
  }, [q])

  return (
    <section>
      <div className="flex items-end justify-between gap-4 mb-4">
        <h1 className="text-3xl font-semibold tracking-tight">Journal</h1>
        <Input placeholder="Search…" value={q} onChange={(e) => setQ(e.target.value)} className="w-56" />
      </div>
      <p className="text-sm text-muted-foreground mb-6">Working notes and short essays.</p>
      <div className="grid md:grid-cols-2 gap-4">
        {filtered.map((j) => (<JournalEntry key={j.title} entry={j} />))}
      </div>
    </section>
  )
}
