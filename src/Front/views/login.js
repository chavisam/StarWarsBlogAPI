import React, { useContext } from "react";
import { Redirect } from "react-router-dom";
import { Context } from "../store/appContext";
import { Login_form } from "../component/login_form";

export const Login = () => {
	const { actions, store } = useContext(Context);
	return (
		<div className="mx-auto text-center">
			<h1 className="text-warning">Welcome to Our Star Wars Blog</h1>

			{store.isLoggedIn ? (
				<Redirect to={"/home"} />
			) : (
				<div>
					<Login_form />
				</div>
			)}
		</div>
	);
};
