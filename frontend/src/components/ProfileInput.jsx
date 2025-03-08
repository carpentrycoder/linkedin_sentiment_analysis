//https://rohan-sharma.netlify.app/
import { useState } from "react";
import axios from "axios"; // Import axios to send requests
import "../app.css";

const ProfileInput = ({ setResult }) => {
  const [profileURL, setProfileURL] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!profileURL) return;
  
    console.log("📤 Sending Profile URL:", profileURL); // Debugging log
  
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/analyze/", {
        profile_url: profileURL,

      });
      console.log(profile_url)
  
      console.log("✅ Received Response:", response.data); // Debugging log
      setResult(response.data);
    } catch (error) {
      console.error("❌ Error fetching analysis:", error.response?.data || error.message);
      setResult({ error: error.response?.data?.error || "Failed to analyze the profile" });
    }
  };
  
  

  return (
    <div>
      <h1>InsightsLens.AI</h1>
      <h2>LinkedIn Profile Sentiment Analysis</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={profileURL}
          onChange={(e) => setProfileURL(e.target.value)}
          placeholder="Paste LinkedIn URL here"
        />
        <button type="submit">Analyze</button>
      </form>
    </div>
  );
};

export default ProfileInput;
