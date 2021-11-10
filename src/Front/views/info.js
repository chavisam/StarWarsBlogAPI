import React, { useContext, useEffect } from "react";
import { Redirect, useParams, Link } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/home.scss";

export const Info = () => {
	const { actions, store } = useContext(Context);
	const params = useParams();
	const pref = store.characterData.result;
	return (
		<div>
			{store.isLoggedIn ? (
				store.characterData.message == "ok" ? (
					<div className="container-fluid">
						<div className="row">
							<div className="col-auto">
								<div className="jumbotron p-5 m-3 mb-5">
									<h1 className="display-4 text-warning">{pref.properties.name}</h1>
									<p className="lead"> {pref.description}</p>
									<button className="btn btn-primary">
										<Link to={"/home/"}>
											<span className="text-warning">Go Back!</span>
										</Link>
									</button>
									<hr className="my-4" />

									{pref.properties.mass ? (
										<div>
											<p>Height: {pref.properties.height} cm.</p>
											<p>Weight: {pref.properties.mass} Kg.</p>
											<p>Hair Color: {pref.properties.hair_color}</p>
											<p>Skin Color: {pref.properties.skin_color} </p>
											<p>Eye Color: {pref.properties.eye_color}</p>
											<p>Gender: {pref.properties.gender}</p>
											<p>Year of Birth: {pref.properties.birth_year} </p>
										</div>
									) : pref.properties.diameter ? (
										<div>
											<p>Diameter: {pref.properties.diameter} </p>
											<p>rotation Period: {pref.properties.rotation_period} </p>
											<p>Orbital Period: {pref.properties.orbital_period}</p>
											<p>Gravity: {pref.properties.gravity} </p>
											<p>Population: {pref.properties.population}</p>
											<p>Climate: {pref.properties.climate}</p>
											<p>terrain: {pref.properties.terrain} </p>
										</div>
									) : (
										<div>
											<p>Model: {pref.properties.model}</p>
											<p>Starship Class: {pref.properties.starship_class}</p>
											<p>Manufacturer: {pref.properties.manufacturer}</p>
											<p>Cost in Credits: {pref.properties.cost_in_credits} </p>
											<p>Lenght: {pref.properties.length}</p>
											<p>Crew: {pref.properties.crew}</p>
											<p>Max Atmosphering Speed: {pref.properties.max_atmosphering_speed} </p>
										</div>
									)}
								</div>
							</div>
							<div className="col-auto offset-4">
								<img
									src={`https://starwars-visualguide.com/assets/img/${
										pref.properties.mass
											? "characters"
											: pref.properties.diameter
											? "planets"
											: "starships"
									}/${pref.uid}.jpg`}
									onError={e => {
										e.target.src = no_dispo;
									}}
									className="characters card-img-top mx-auto"
									alt="..."
								/>
							</div>
						</div>
					</div>
				) : (
					<div className="row">
						<div className="spinner-grow text-success mx-auto" role="status">
							<span className="sr-only">Loading...</span>
						</div>
						<span className="sr-only">Loading...</span>
					</div>
				)
			) : (
				<Redirect to={"/"} />
			)}
		</div>
	);
};
