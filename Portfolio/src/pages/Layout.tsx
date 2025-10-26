import { Outlet } from 'react-router-dom'
import { Navbar } from '@/components/navbar'
import { Footer } from '@/components/footer'
import { ThemeToggle } from '@/components/theme-toggle'

export function Layout() {
  return (
    <div className="min-h-svh flex flex-col">
      <Navbar />
      <main className="flex-1 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 animate-enter">
        <Outlet />
      </main>
      <Footer />
      <ThemeToggle />
    </div>
  )
}
