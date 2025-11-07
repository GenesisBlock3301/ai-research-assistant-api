'use client';

import React, { useState } from "react";
import ProtectedRouter from "@/components/auth/ProtectedRouter";

const ChatPage = () => {
    const [query, setQuery] = useState("");
    const [response, setResponse] = useState("Here your response will appear...");
    const [loading, setLoading] = useState(false);
    const [documents, setDocuments] = useState(["Doc 1", "Doc 2", "Doc 3", "Doc 4"]);

    const handleQuery = () => {
        if (!query.trim()) return;

        setLoading(true);
        setResponse("");
        setTimeout(() => {
            setResponse(`Response for: "${query}"`);
            setLoading(false);
        }, 2000);
    };

    const handleDelete = (indexToDelete: any) => {
        setDocuments((prevDocs) => prevDocs.filter((_, index) => index !== indexToDelete));
    };

    return (
        <ProtectedRouter>
            <div className="grid grid-cols-12 gap-4 p-4 min-h-screen bg-gray-50">
                <div className="col-span-12 md:col-span-8 flex flex-col gap-4 py-4">
                    <div className="flex gap-2">
                        <input
                            type="text"
                            placeholder="Enter your query"
                            className="p-2 border rounded placeholder-gray-400 text-white w-full bg-blue-950 focus:outline-none focus:ring-2 focus:ring-blue-500"
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                        />
                        <button
                            onClick={handleQuery}
                            disabled={loading}
                            className={`px-4 rounded text-white transition ${
                                loading
                                    ? "bg-blue-400 cursor-not-allowed"
                                    : "bg-blue-600 hover:bg-blue-700"
                            }`}
                        >
                            {loading ? "Sending..." : "Send"}
                        </button>
                    </div>

                    {/* Response area */}
                    <div className="flex-1 p-4 border rounded bg-blue-950 text-white overflow-auto relative">
                        {loading ? (
                            <div className="flex justify-center items-center h-full">
                                <div className="w-10 h-10 border-4 border-white border-dashed rounded-full animate-spin"></div>
                            </div>
                        ) : (
                            <div>{response}</div>
                        )}
                    </div>
                </div>
                <div className="col-span-12 md:col-span-4 p-4 border rounded bg-blue-950 h-full">
                    <h2 className="font-bold mb-4 text-white text-lg">Documents</h2>
                    <ul className="space-y-2 max-h-[500px] overflow-auto">
                        {documents.length > 0 ? (
                            documents.map((doc, index) => (
                                <li
                                    key={index}
                                    className="flex justify-between items-center p-2 border rounded hover:bg-gray-800 text-white transition"
                                >
                                    <span>{doc}</span>
                                    <button
                                        onClick={() => handleDelete(index)}
                                        className="bg-red-500 text-white px-2 py-1 text-sm rounded hover:bg-red-600 transition"
                                    >
                                        Delete
                                    </button>
                                </li>
                            ))
                        ) : (
                            <p className="text-gray-300 italic">No documents available.</p>
                        )}
                    </ul>
                </div>
            </div>
        </ProtectedRouter>
    );
};

export default ChatPage;
