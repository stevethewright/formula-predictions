import Link from "next/link";

async function getNextRace() {
  const res = await fetch(`${process.env.APP_URL}/api/event/next`);
  const data = await res.json();
  return { data };
}

export default async function Navbar() {
  const { data } = await getNextRace();
  return (
    <nav>
      <div className="flex border-b-2 border-red-800 bg-black p-5 text-white">
        <div className="flex">
          <div className="font-black">Formula Predictions</div>
          <div className="font-black">|</div>
          <div>{data.testContent[0].meeting_name}</div>
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
