import React from "react";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Notes from "./components/Notes";

function App() {
  return (
    <div className="flex flex-col justify-between bg-gray-200 min-h-screen">
      <Navbar />
      <Notes />
      <Footer />
    </div>
  );
}

export default App;
