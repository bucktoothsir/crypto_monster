import React from "react";

const TextArea = (prop) => {
    const title = prop.title;
    const onInput = prop.onInput
    const value = prop.value

    return (
        <div className="w-1/4 h-full mx-4">
            <header className="w-full h-1/6 border-2 border-green-700 rounded-t-lg bg-white">
                <p className="ml-1 mt-3 h-1/6 text-2xl font-bold font-mono align-bottom text-center text-green-700"> {title} </p>
            </header>
            <textarea
                className="w-full h-5/6 text-xl font-sans antialiased font-light text-green-700 focus:outline-none focus:ring-4 focus:ring-green-700 focus:border-transparent border-b-2 border-l-2 border-r-2 border-green-700 resize-none bg-white rounded-b-lg" 
                value={value} 
                onInput={onInput}
            >
            </textarea>
        </div>
    );
}

export default TextArea;