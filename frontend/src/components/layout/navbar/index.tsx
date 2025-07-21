"use client";

import { Event } from "@/interfaces/Event";
import Link from "next/link";
import { useEffect, useState } from "react";

export default function Navbar() {
  const [data, setData] = useState<Event | undefined>(undefined);

  const getNextEvent = async () => {
    const res = await fetch("/api/event/next");
    const data: Event = await res.json();
    setData(data);
  };

  useEffect(() => {
    getNextEvent();
  }, []);

  return (
    <nav>
      <div className="flex border-b-2 border-red-800 bg-black p-5 text-white">
        <div className="flex">
          <div className="font-black">Formula Predictions</div>
          <div className="font-black">|</div>
          {data !== undefined ? (
            <>
              <div>{data.officialEventName}</div>
            </>
          ) : (
            <div></div>
          )}
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
