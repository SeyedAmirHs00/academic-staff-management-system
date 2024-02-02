"use client";

import Link from "next/link";
import { useState } from "react";

const tabs = [
  "Dashboard",
  "Staff",
  "Buildings",
  "Departments",
  "Employees",
  "Faculties",
  "Fields",
  "Laboratories",
  "Libraries",
  "Offices",
  "Professors",
  "Researchers",
  "Researchs",
  "Schedules",
];

const GenerateButtonStyle = (active: number, index: number) => {
  if (active == index) {
    return "bg-main-peach";
  } else {
    return "bg-main-peach/50";
  }
};

const ManageMenu = () => {
  const [active, setActive] = useState(0);
  const buttons = tabs.map((tab, index) => (
    <Link
      href={tab.toLowerCase()}
      className={GenerateButtonStyle(active, index)}
      onClick={() => {
        setActive(index);
      }}
      key={index}
    >
      {tab}
    </Link>
  ));

  return <nav>{buttons}</nav>;
};

export default ManageMenu;
