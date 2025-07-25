"use server";

import { NextResponse } from "next/server";

export async function GET() {
  const response = await fetch(`${process.env.API_URL}/events/next`);
  const data = await response.json();
  return NextResponse.json(data);
}
