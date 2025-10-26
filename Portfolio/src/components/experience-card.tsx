import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

type Exp = { company: string; role: string; period: string; location: string; highlights: string[]; stack: string[] }
export function ExperienceCard({ exp }: { exp: Exp }) {
  return (
    <Card className="h-full">
      <CardHeader>
        <div className="flex items-start justify-between gap-3">
          <div>
            <CardTitle className="text-lg">{exp.role}</CardTitle>
            <p className="text-sm text-muted-foreground">{exp.company}</p>
          </div>
          <Badge variant="outline" className="rounded-full whitespace-nowrap">{exp.period}</Badge>
        </div>
      </CardHeader>
      <CardContent className="space-y-3">
        <p className="text-xs text-muted-foreground">{exp.location}</p>
        <ul className="space-y-2 text-sm list-disc pl-5">
          {exp.highlights.map((h) => (<li key={h}>{h}</li>))}
        </ul>
        <div className="mt-2 flex flex-wrap gap-2">
          {exp.stack.map((s) => (<Badge key={s} variant="secondary" className="rounded-full">{s}</Badge>))}
        </div>
      </CardContent>
    </Card>
  )
}
