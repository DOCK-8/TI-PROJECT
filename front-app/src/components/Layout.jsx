// src/components/Layout.jsx
import { Outlet } from "react-router-dom";
import "../styles/background.css";
import "../styles/logo.css";

export default function Layout() {
  const bubbles = [
    { i: 17, x: "44%", delay: "2.3s", size: "32px" },
    { i: 14, x: "91%", delay: "0.7s", size: "24px" },
    { i: 21, x: "21%", delay: "3.1s", size: "38px" },
    { i: 15, x: "18%", delay: "1.6s", size: "28px" },
    { i: 23, x: "70%", delay: "4.5s", size: "40px" },
    { i: 11, x: "33%", delay: "0.3s", size: "22px" },
    { i: 18, x: "5%", delay: "2.8s", size: "30px" },
    { i: 26, x: "60%", delay: "1.2s", size: "36px" },
    { i: 13, x: "78%", delay: "3.7s", size: "20px" },
    { i: 22, x: "39%", delay: "0.9s", size: "42px" },
    { i: 19, x: "74%", delay: "1.4s", size: "26px" },
    { i: 12, x: "7%", delay: "4.1s", size: "38px" },
    { i: 24, x: "55%", delay: "2.6s", size: "34px" },
    { i: 20, x: "12%", delay: "1.8s", size: "30px" },
    { i: 14, x: "62%", delay: "2.0s", size: "24px" },
    { i: 16, x: "96%", delay: "0.5s", size: "18px" },
    { i: 25, x: "35%", delay: "3.4s", size: "40px" },
    { i: 18, x: "21%", delay: "0.1s", size: "28px" },
  ];

  return (
    <>
      <div className="bgk-container">
        <div className="bubbles">
          {bubbles.map((bubble, idx) => (
            <span
              key={idx}
              style={{
                "--i": bubble.i,
                "--x": bubble.x,
                "--delay": bubble.delay,
                "--size": bubble.size,
              }}
            ></span>
          ))}
        </div>
      </div>

      <div className="content">
        <Outlet />
      </div>
    </>
  );
}
