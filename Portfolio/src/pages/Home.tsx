import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import headshot from "@/assets/TennisHeadshot2.jpg";
import { PROFILE } from "@/lib/data/profile";
import { motion } from "framer-motion";

export function Home() {
  return (
    <div className="grid lg:grid-cols-3 gap-6">
      <div className="lg:col-span-2 space-y-6">
        <motion.div
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
        >
          <Card className="overflow-hidden">
            <div className="relative">
              <div className="h-48 sm:h-58 bg-gradient-to-br from-blue-500/40 via-violet-500/30 to-emerald-400/40 animate-shimmer bg-[length:200%_100%]" />{" "}
              <div className="absolute -bottom-10 left-6 h-40 w-40 sm:h-29 sm:w-29 rounded-3xl ring-2 ring-white/70 dark:ring-black/40 shadow-xl overflow-hidden flex items-center justify-center">
                <img
                  loading="lazy"
                  decoding="async"
                  fetchPriority="low"
                  src={headshot}
                  alt="Luka"
                  className="h-full w-full object-cover"
                />
              </div>
            </div>
            <CardContent className="pt-16 sm:pt-20">
              <h1 className="text-3xl font-semibold tracking-tight">
                {PROFILE.name}
              </h1>
              <p className="mt-1 text-muted-foreground">
                {PROFILE.title} · {PROFILE.location}
              </p>
              <p className="mt-4 max-w-2xl leading-relaxed">
                {PROFILE.summary}
              </p>
              <div className="mt-4 flex flex-wrap gap-2">
                {PROFILE.keywords.map((t) => (
                  <Badge key={t} variant="secondary" className="rounded-full">
                    {t}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>
        </motion.div>

        <section>
          <h2 className="text-2xl font-semibold tracking-tight mb-3">
            What I focus on
          </h2>
          <div className="grid sm:grid-cols-2 gap-4">
            {PROFILE.principles.map((b) => (
              <motion.div
                key={b.title}
                initial={{ opacity: 0, y: 8 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.35 }}
              >
                <Card className="shadow-md hover:shadow-[0_6px_24px_rgba(16,185,129,0.25)] transition-all duration-300">
                  <CardHeader className="pb-2">
                    <CardTitle className="text-base">{b.title}</CardTitle>
                  </CardHeader>
                  <CardContent className="text-sm text-muted-foreground">
                    {b.body}
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>
        </section>
      </div>

      {/* Right column */}
      <div className="space-y-6">
        {/* Get in touch nicer */}
        <div className="rounded-2xl border bg-card/80 backdrop-blur shadow-sm">
          <div className="p-6 pb-2">
            <h3 className="text-lg font-semibold tracking-tight">
              Get in touch
            </h3>
            <p className="text-sm text-muted-foreground mt-1">
              I’m open to interesting problems, collaborative builds, and
              learning opportunities.
            </p>

            <div className="mt-4 grid grid-cols-1 sm:grid-cols-3 gap-2">
              <a
                href={`mailto:${PROFILE.email}`}
                className="flex items-center justify-center gap-2 rounded-xl border px-4 py-2 text-sm hover:bg-secondary/70 transition"
              >
                Email
              </a>
              <a
                href={PROFILE.links[0].href}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-center gap-2 rounded-xl border px-4 py-2 text-sm hover:bg-secondary/70 transition"
              >
                GitHub
              </a>
              <a
                href={PROFILE.links[1].href}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-center gap-2 rounded-xl border px-4 py-2 text-sm hover:bg-secondary/70 transition"
              >
                LinkedIn
              </a>
            </div>
          </div>
        </div>

        {/* You can keep or customize your "Currently" card here if desired */}
      </div>
    </div>
  );
}
