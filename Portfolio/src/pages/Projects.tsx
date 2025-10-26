import { PROJECTS } from '@/lib/data/projects'
import { ProjectCard } from '@/components/project-card'
import { motion } from 'framer-motion'

export function Projects() {
  return (
    <section>
      <h1 className="text-3xl font-semibold tracking-tight mb-4">Passion Projects</h1>
      <p className="text-sm text-muted-foreground mb-6">A few things I’ve built to learn, explore, or make life easier.</p>
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {PROJECTS.map((p, i) => (
          <motion.div key={p.name} initial={{ opacity: 0, y: 8 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: .35, delay: i * 0.04 }}>
            <ProjectCard project={p} />
          </motion.div>
        ))}
      </div>
    </section>
  )
}
