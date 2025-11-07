import React from 'react'

const RegisterForm = () => {
    return (
        <form action=""
              className="bg-white p-8 rounded shadow-md w-96 flex flex-col space-y-4"
        >
            <h2 className="text-xl font-bold text-center text-black">Register</h2>
            <input
                type="email"
                placeholder="Email"
                name="email"
                className="p-2 border rounded placeholder-gray-700 text-black"
            />
            <input
                type="password"
                placeholder="Password"
                name="password"
                className="p-2 border rounded placeholder-gray-700 text-black"
            />
            <input
                type="password"
                placeholder="Confirm Password"
                name="confirmPassword"
                className="p-2 border rounded placeholder-gray-700 text-black"
            />
            <button
                type="submit"
                className="bg-green-600 text-white py-2 rounded hover:bg-green-700"
            >
                Register
            </button>
        </form>
    )
}
export default RegisterForm
