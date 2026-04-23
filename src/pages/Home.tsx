import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-12 min-h-[calc(100vh-3.5rem)]">
      <section className="max-w-5xl mx-auto text-center mb-8">
        <p className="inline-flex items-center rounded-full border border-border bg-secondary px-3 py-1 text-xs tracking-wide uppercase text-muted-foreground mb-4">
          Wiki Navigation
        </p>
        <h1 className="text-4xl font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
          My Wiki Home
        </h1>
        <p className="text-lg text-muted-foreground mt-4 max-w-2xl mx-auto">
          放大版导航栏首页：仅用于站内导航，保持项目内部闭环。
        </p>
      </section>

      <section className="max-w-4xl mx-auto grid grid-cols-1 sm:grid-cols-2 gap-4">
        <Link
          to="/wiki"
          className="group rounded-xl border border-border bg-card p-5 text-left transition-all hover:-translate-y-0.5 hover:border-ring hover:shadow-lg"
        >
          <span className="text-xs uppercase tracking-wide text-muted-foreground">Primary</span>
          <h2 className="mt-2 text-xl font-semibold">进入 Wiki</h2>
          <p className="mt-2 text-sm text-muted-foreground">打开文档侧边栏并浏览全部知识条目。</p>
        </Link>

        <Link
          to="/"
          className="group rounded-xl border border-border bg-card p-5 text-left transition-all hover:-translate-y-0.5 hover:border-ring hover:shadow-lg"
        >
          <span className="text-xs uppercase tracking-wide text-muted-foreground">Current Page</span>
          <h2 className="mt-2 text-xl font-semibold">首页导航</h2>
          <p className="mt-2 text-sm text-muted-foreground">返回当前首页，作为站内总入口与导览面板。</p>
        </Link>
      </section>
    </div>
  );
}
