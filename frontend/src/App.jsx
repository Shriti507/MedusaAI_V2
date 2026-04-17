import React, { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [report, setReport] = useState("");
  const [sources, setSources] = useState([]);

  const generate = async () => {
    const res = await axios.post("http://127.0.0.1:8000/research", {
      query,
    });

    setReport(res.data.final_report);
    setSources(res.data.filtered_results);
  };

  const exportPDF = async () => {
    await axios.post("http://127.0.0.1:8000/export/pdf", {
      text: report,
    });
    alert("PDF exported!");
  };

  const exportMD = async () => {
    await axios.post("http://127.0.0.1:8000/export/md", {
      text: report,
    });
    alert("Markdown exported!");
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Research Assistant</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter research topic"
      />

      <button onClick={generate}>Generate</button>

      <h2>Report</h2>
      <pre>{report}</pre>

      <h2>Sources</h2>
      {sources.map((s, i) => (
        <p key={i}>{s.href}</p>
      ))}

      <button onClick={exportPDF}>Export PDF</button>
      <button onClick={exportMD}>Export Markdown</button>
    </div>
  );
}

export default App;