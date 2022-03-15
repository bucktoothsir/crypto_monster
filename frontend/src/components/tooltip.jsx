import React from "react";
import { BiCommentError } from "react-icons/bi";

const Tooltip = () => {
    return (
        <div>
            <button className="float-right" data-tooltip-target="decode-tooltip" type="button">
                <p style={{color: "#19a822"}}> <BiCommentError /> </p>
            </button>
            <div id="decode-tooltip" role="tooltip" className="inline-block absolute invisible z-10 py-2 px-3 font-medium text-white bg-green-400 rounded-lg shadow-sm opacity-0 transition-opacity duration-300 tooltip dark:bg-gray-700">
                <p className="text-white font-bold text-sm antialiased font-mono text-justify">
                Wanna decode without key?
                <br></br>
                Just leave the key or key length empty!
                <br></br>
                Note that the longer the ciphertext, the better it works.
                </p>
                <div className="tooltip-arrow" data-popper-arrow>
                </div>
            </div>
        </div>
    )
}

export default Tooltip;