import { Moon, SunMedium } from "lucide-react";
import { useEffect, useState } from "react";

type DarkAccent = "onyx";

const THEME_STORAGE_KEY = "portfolio-theme";

const getInitialTheme = () => {
  if (typeof window === "undefined") {
    return false; // prefer light by default when SSR/undefined window
  }
  const stored = localStorage.getItem(THEME_STORAGE_KEY);
  if (stored === "dark") return true;
  if (stored === "light") return false;
  // No stored preference: prefer light
  return false;
};

const DEFAULT_ACCENT: DarkAccent = "onyx";

export function ThemeToggle() {
  const [dark, setDark] = useState<boolean>(() => getInitialTheme());
  const [accent] = useState<DarkAccent>(DEFAULT_ACCENT);

  useEffect(() => {
    const root = document.documentElement;
    if (dark) {
      root.classList.add("dark");
      localStorage.setItem(THEME_STORAGE_KEY, "dark");
    } else {
      root.classList.remove("dark");
      localStorage.setItem(THEME_STORAGE_KEY, "light");
    }
  }, [dark]);

  useEffect(() => {
    const root = document.documentElement;
    root.dataset.darkAccent = accent;
  }, [accent]);

  return (
    <div className="fixed bottom-4 right-4 flex flex-col items-end gap-3 text-left">
      <button
        aria-label={dark ? "Switch to light theme" : "Switch to dark theme"}
        onClick={() => setDark((d) => !d)}
        className="inline-flex items-center rounded-full border border-border/50 bg-background p-2.5 shadow-lg backdrop-blur-md transition hover:bg-secondary/80"
      >
        {dark ? <SunMedium className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
      </button>
    </div>
  );
}
