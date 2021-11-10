import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import no_dispo from "./../../img/nodispo.jpg";

export const Card = props => {
	const { actions, store } = useContext(Context);

	useEffect(() => {
		store.isLoggedIn ? actions.loadData(`${props.type_info}`) : "";
	}, []);

	return (
		<div className="scroll">
			{store[props.type_info].length > 0 ? (
				store[props.type_info].map((item, index) => {
					return (
						<div key={index} className="card">
							<div className="row">
								<div className="col-auto mx-auto">
									<img
										src={`https://starwars-visualguide.com/assets/img/${
											props.type_info == "people" ? "characters" : props.type_info
										}/${item.uid}.jpg`}
										onError={e => {
											e.target.src = no_dispo;
										}}
										className="characters card-img-top mx-auto"
										alt="..."
									/>
								</div>
							</div>
							<div className="card-body">
								<h5 className="card-title text-danger">{item.name}</h5>

								<button
									className="btn btn-primary mb-2"
									onClick={() => actions.getCharacterData(item.uid, props.type_info)}>
									<Link to={"/info/" + index + 1}>
										<span className="text-warning ">Más Info</span>
									</Link>
								</button>
							</div>
						</div>
					);
				})
			) : (
				<div className="spinner-grow text-success mx-auto" role="status">
					<span className="sr-only">Loading...</span>
				</div>
			)}
		</div>
	);
};

Card.propTypes = {
	type_info: PropTypes.string
};
