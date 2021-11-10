import React, { useContext } from "react";
import { Link } from "react-router-dom";
import logo from "./../../img/logostarwars.png";
import { Context } from "../store/appContext";

export const Navbar = () => {
	const { actions, store } = useContext(Context);
	return (
		<nav className="navbar navbar-light bg-light mb-3">
			<Link to="/home">
				<span className="navbar-brand mb-0 h1">
					<img src={logo} alt="logo" id="logo" />
				</span>
			</Link>
			<div className="ml-auto">
				<span>
					{store.isLoggedIn ? (
						<div>
							<button className="btn btn-secondary" onClick={() => actions.logout()}>
								LogOut
							</button>
						</div>
					) : (
						""
					)}
				</span>
				<span className="">
					<Link to="/demo">
						<button className="btn btn-primary ml-3">Favorites</button>
					</Link>
				</span>
			</div>
		</nav>
	);
};
