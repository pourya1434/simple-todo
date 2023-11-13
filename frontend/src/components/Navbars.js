import React, { useState } from "react";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Navbar";
import { Link } from "react-router-dom";

function Navbars() {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const [error, setError] = useState("");

  const login = async (user = null) => {
    setUser(user);
  };
  const signup = async (user = null) => {
    setUser(user);
  };
  const logout = async () => {
    setUser(null);
  };

  return (
    <div className="App">
      <Navbar bg="secondary" variant="dark">
        <div className="container-fluid">
          <Navbar.Brand>To Do</Navbar.Brand>
          <Nav className="me-auto">
            <Container>
              <Link className="nav-link" to={"/todos"}>
                Todos
              </Link>
              {user ? (
                <Link className="nav-link">Logout ({user})</Link>
              ) : (
                <>
                  <Link className="nav-link" to={"/login"}>
                    Login
                  </Link>
                  <Link className="nav-link" to={"/signup"}>
                    Sign Up
                  </Link>
                </>
              )}
            </Container>
          </Nav>
        </div>
      </Navbar>
    </div>
  );
}

export default Navbars;
