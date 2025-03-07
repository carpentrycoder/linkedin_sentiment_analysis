import { useState } from "react";
import ProfileInput from "./components/ProfileInput";
import Results from "./components/Results";
import './app.css';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div>
      <ProfileInput setResult={setResult} />
      <Results result={result} />
    </div>
  );
}

export default App;
