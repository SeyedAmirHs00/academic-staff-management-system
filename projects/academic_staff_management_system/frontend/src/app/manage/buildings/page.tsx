import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import BuildingForm from "@/app/components/BuildingForm";

const page = () => {
  const find_building_style =
    "bg-main-grey py-1 px-2 ml-5 mt-3 text-main-dark opacity-60 hover:opacity-100 duration-300 rounded-md";
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <h3 className="text-main-peach text-2xl font-bold px-6 py-0 mt-5">
            Add, Edit & Remove Building
          </h3>
          <button className={find_building_style}>Find Building</button>
          <form action="" method="">
            <BuildingForm></BuildingForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
