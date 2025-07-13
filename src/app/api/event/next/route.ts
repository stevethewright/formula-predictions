export async function GET() {
  let testContent = "{ message: 'test'}";
  await fetch("https://api.openf1.org/v1/meetings?meeting_key=latest")
    .then((response) => response.json())
    .then((jsonContent) => (testContent = jsonContent));

  return Response.json({ testContent });
}
