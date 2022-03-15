import React from "react";
import DropdownOption from "./dropdownOption"


const DropdownCard = (prop) => {
    const options = prop.options;
    const onClick = prop.onClick;
    return (
        <div className="mt-2 z-10 list-none bg-green-500 rounded divide-y divide-green-700 shadow dark:bg-green-700">
            <ul className="py-1">
                {
                    options.map(
                        (option, i) => <DropdownOption optionKey={i} option={option} onClick={onClick}/>
                    )
                }
            </ul>
        </div>
    )
}

export default DropdownCard;