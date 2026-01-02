import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-12 flex flex-col items-center justify-center min-h-[calc(100vh-3.5rem)] text-center">
      <h1 className="text-4xl font-extrabold tracking-tight lg:text-5xl mb-4">
        Welcome to My Personal Space
      </h1>
      <p className="text-xl text-muted-foreground mb-8 max-w-[600px]">
        A place where I document my learning journey, thoughts, and projects.
      </p>
      <div className="flex gap-4">
        <Link 
          to="/wiki" 
          className="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2"
        >
          Explore Wiki
        </Link>
        <a 
          href="https://github.com/zf-li23/personal-wiki-site" 
          target="_blank" 
          rel="noreferrer"
          className="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2"
        >
          GitHub Profile
        </a>
      </div>
    </div>
  );
}
