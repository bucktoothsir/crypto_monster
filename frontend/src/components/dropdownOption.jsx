import React from "react";


const DropdownOption = (prop) => {
    const option = prop.option;
    const optionKey = prop.optionKey;
    const onClick = prop.onClick;

    return (
        <li key={optionKey}>
            <p className="block font-bold antialiased font-mono py-2 px-4 text-lg text-white hover:bg-green-700 dark:hover:bg-green-600 dark:text-green-200 dark:hover:text-white" onClick={onClick}>
                {option}
            </p>
        </li>
    )
}

export default DropdownOption;