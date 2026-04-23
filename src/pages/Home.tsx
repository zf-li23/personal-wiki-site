import { Link } from 'react-router-dom';
import { wikiData } from '@/data/wikiData';

function formatWikiLabel(slug: string, title: string) {
  const number = slug.match(/^[\d.]+/)?.[0];
  return number ? `${number} ${title}` : title;
}

function buildWikiPath(...segments: string[]) {
  return `/${segments.filter(Boolean).join('/')}`.replace(/\/+/g, '/');
}

export default function Home() {
  const primaryEntry = wikiData[0];

  return (
    <div className="relative overflow-hidden min-h-[calc(100vh-3.5rem)]">
      <div className="absolute inset-0 -z-10 bg-[radial-gradient(circle_at_top_left,_rgba(120,119,198,0.16),_transparent_32%),radial-gradient(circle_at_top_right,_rgba(56,189,248,0.12),_transparent_28%),linear-gradient(180deg,_rgba(248,250,252,0.7),_rgba(255,255,255,0))] dark:bg-[radial-gradient(circle_at_top_left,_rgba(120,119,198,0.18),_transparent_32%),radial-gradient(circle_at_top_right,_rgba(56,189,248,0.12),_transparent_28%),linear-gradient(180deg,_rgba(15,23,42,0.7),_rgba(15,23,42,0))]" />
      <div className="container mx-auto px-4 py-10 md:py-14">
        <section className="max-w-5xl mx-auto">
          <div className="inline-flex items-center gap-2 rounded-full border border-border bg-background/70 px-4 py-1.5 text-xs tracking-[0.24em] uppercase text-muted-foreground shadow-sm backdrop-blur">
            Personal knowledge base
          </div>
          <div className="mt-6 grid gap-8 lg:grid-cols-[1.2fr_0.8fr] lg:items-end">
            <div>
              <h1 className="text-4xl font-black tracking-tight sm:text-5xl lg:text-6xl">
                My Personal Wiki
              </h1>
              <p className="mt-4 max-w-2xl text-base leading-7 text-muted-foreground sm:text-lg">
                这里只保留一个入口：知识库本身。下面的目录把一级章节放大展示，方便直接跳进内容层。
              </p>
            </div>
            {primaryEntry && (
              <Link
                to={buildWikiPath(primaryEntry.slug)}
                className="group inline-flex w-full items-center justify-between rounded-2xl border border-border bg-background/85 px-5 py-4 shadow-lg shadow-black/5 backdrop-blur transition-all hover:-translate-y-0.5 hover:border-primary/40 hover:shadow-xl dark:shadow-black/20"
              >
                <div>
                  <p className="text-xs uppercase tracking-[0.2em] text-muted-foreground">Start reading</p>
                  <h2 className="mt-1 text-xl font-semibold">进入 {primaryEntry.title}</h2>
                </div>
                <span className="text-sm font-medium text-primary transition-transform group-hover:translate-x-1">→</span>
              </Link>
            )}
          </div>
        </section>

        <section className="mx-auto mt-10 max-w-6xl space-y-6">
          {wikiData.map((rootPage) => {
            const rootPath = buildWikiPath(rootPage.slug);
            const children = rootPage.children ?? [];

            return (
              <article key={rootPage.id} className="rounded-[2rem] border border-border/80 bg-background/80 p-5 shadow-[0_20px_60px_rgba(15,23,42,0.07)] backdrop-blur-sm md:p-6">
                <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                  <Link to={rootPath} className="group max-w-2xl">
                    <p className="text-xs font-medium uppercase tracking-[0.2em] text-muted-foreground">
                      {rootPage.slug.match(/^[\d.]+/)?.[0] ?? 'Section'}
                    </p>
                    <h2 className="mt-1 text-2xl font-bold tracking-tight transition-colors group-hover:text-primary sm:text-3xl">
                      {rootPage.title}
                    </h2>
                    <p className="mt-2 text-sm leading-6 text-muted-foreground">
                      {children.length > 0 ? `${children.length} 个下级目录` : '直接进入该章节正文。'}
                    </p>
                  </Link>

                  <div className="rounded-2xl border border-border bg-muted/30 px-4 py-3 text-sm text-muted-foreground">
                    <div className="font-medium text-foreground">一级导航</div>
                    <div className="mt-1">点击任一块直接跳转，不再经过多余的站点层级。</div>
                  </div>
                </div>

                {children.length > 0 && (
                  <div className="mt-5 grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
                    {children.map((child) => {
                      const childPath = buildWikiPath(rootPage.slug, child.slug);

                      return (
                        <Link
                          key={child.id}
                          to={childPath}
                          className="group rounded-2xl border border-border bg-card/80 p-4 transition-all hover:-translate-y-0.5 hover:border-primary/30 hover:bg-card hover:shadow-md"
                        >
                          <p className="text-xs font-medium uppercase tracking-[0.18em] text-muted-foreground">
                            {child.slug.match(/^[\d.]+/)?.[0] ?? 'Chapter'}
                          </p>
                          <h3 className="mt-2 text-lg font-semibold tracking-tight transition-colors group-hover:text-primary">
                            {formatWikiLabel(child.slug, child.title)}
                          </h3>
                          <p className="mt-2 text-sm text-muted-foreground">
                            {child.children && child.children.length > 0
                              ? `${child.children.length} 个更深层章节`
                              : '进入具体知识点正文'}
                          </p>
                        </Link>
                      );
                    })}
                  </div>
                )}
              </article>
            );
          })}
        </section>
      </div>
    </div>
  );
}
