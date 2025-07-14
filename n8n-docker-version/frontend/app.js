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

  const res = await fetch("https://manavsaha.app.n8n.cloud/webhook/08109d18-ae3c-43df-b097-0f0107624158", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const text = await res.text();
  console.log("Raw response text:", text);

  let data;
  try {
    data = text ? JSON.parse(text) : {};
  } catch (err) {
    console.error("JSON parse error:", err);
    data = { error: "Invalid JSON response" };
  }

  // If response is an array with an object containing "output"
if (Array.isArray(data) && data[0]?.output) {
  document.getElementById("output").textContent = data[0].output;
} else {
  document.getElementById("output").textContent = "Unexpected response format.";
}

}
