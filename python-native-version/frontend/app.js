async function submitReflection() {
  const reflection = document.getElementById("reflection").value;
  const session_context = {
    user_id: "user123",
    user_role: "PM",
    journey_stage: "brainstorm",
    intent: "summarize"
  };

  const payload = {
    reflection,
    project_data: {},
    emotional_metadata: {},
    session_context
  };

  const res = await fetch("http://localhost:8000/run-agent", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await res.json();
  document.getElementById("output").textContent = JSON.stringify(data, null, 2);
}
