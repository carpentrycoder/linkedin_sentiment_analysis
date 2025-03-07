import React from "react";

const Results = ({ result }) => {
  if (!result) {
    return <p>No results yet. Submit a profile to analyze.</p>;
  }

  return (
    <div>
      <h2>Analysis Results</h2>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
};

export default Results;
