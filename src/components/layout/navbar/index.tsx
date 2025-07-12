import Link from "next/link";

export function Navbar() {
  return (
    <nav>
      <div className="flex border-b-2 border-red-800 bg-black p-5 text-white">
        <div className="flex">
          <div className="font-black">Formula Predictions</div>
          <div className="font-black">|</div>
          <div>(Next Race Details)</div>
        </div>
        <div className="ml-auto flex gap-3">
          <div>(points status)</div>
          <div>(username)</div>
          <Link className="hover:text-red-700" href="/">
            Home
          </Link>
          <Link className="hover:text-red-700" href="/predict">
            Predict
          </Link>
          <Link className="hover:text-red-700" href="/settings">
            Settings
          </Link>
        </div>
      </div>
    </nav>
  );
}
