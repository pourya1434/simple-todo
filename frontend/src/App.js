import React from "react";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="flex flex-col justify-between bg-gray-200 min-h-screen">
      <Navbar />
      <Footer />
    </div>
  );
}

export default App;
