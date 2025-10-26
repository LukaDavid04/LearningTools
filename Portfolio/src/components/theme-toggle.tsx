import { Moon, SunMedium } from 'lucide-react'
import { useEffect, useState } from 'react'

export function ThemeToggle() {
  const [dark, setDark] = useState(true)
  useEffect(() => {
    const r = document.documentElement
    dark ? r.classList.add('dark') : r.classList.remove('dark')
  }, [dark])
  return (
    <button aria-label="Toggle theme" onClick={() => setDark((d) => !d)} className="fixed bottom-4 right-4 rounded-full border px-3 py-2 text-sm bg-background shadow-sm hover:bg-secondary">
      {dark ? <SunMedium className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
    </button>
  )
}
