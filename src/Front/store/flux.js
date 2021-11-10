const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			//we create the variable to login
			isLoggedIn: false,
			//we create the variable for favorites
			favorites: 0,
			//we create variable Characters
			nextpeople: null,
			nextplanets: null,
			nextstarships: null,
			previouspeople: null,
			previousplanets: null,
			previousstarships: null,

			people: [],
			planets: [],
			starships: [],
			characterData: {}
		},
		actions: {
			//LOGIN
			login: _bool => setStore({ isLoggedIn: true }),
			// LOGOUT
			logout: _bool => setStore({ isLoggedIn: false }),

			//we use the starwars API
			loadData: type_info => {
				fetch(`https://www.swapi.tech/api/${type_info}`)
					.then(response => {
						//console.log(response.ok);
						console.log(response.status);
						return response.json();
					})
					.then(data => {
						setStore({ [type_info]: data.results });
						setStore({ ["next" + type_info]: data.next });
					})
					.catch(error => console.error(error));
			},

			//function to see 10 more
			ten_more: data => {
				const store = getStore();

				let uri = store[`next${data}`];

				fetch(uri)
					.then(response => {
						console.log(response.status);
						return response.json();
					})
					.then(resp => {
						console.log(resp.results);
						setStore({ [data]: resp.results });
						setStore({ ["next" + data]: resp.next });
						setStore({ ["previous" + data]: resp.previous });
					})
					.catch(error => console.error(error));
			},

			//function to see 10 PREVIOUS
			ten_previous: data => {
				const store = getStore();

				let uri = store[`previous${data}`];

				fetch(uri)
					.then(response => {
						console.log(response.status);
						return response.json();
					})
					.then(resp => {
						console.log(resp.results);
						setStore({ [data]: resp.results });
						setStore({ ["next" + data]: resp.next });
						setStore({ ["previous" + data]: resp.previous });
					})
					.catch(error => console.error(error));
			},
			//FUNCTION TO FETCH A CHARACTER DATA
			getCharacterData: (id, type) => {
				setStore({ characterData: {} });
				fetch(`https://www.swapi.tech/api/${type}/${id}`)
					.then(response => {
						console.log(response.status);
						return response.json();
					})
					.then(resp => {
						setStore({ characterData: resp });
					})
					.catch(error => console.error(error));
			},

			//FUNCTION TO CREATE TOKEN
			generate_token: async (email_received, password_received) => {
				const resp = await fetch(`https://3000-teal-blackbird-ivqacksq.ws-eu18.gitpod.io/token`, {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({ email: email_received, password: password_received })
				});

				if (!resp.ok) throw Error("There was a problem in the login request");

				if (resp.status === 401) {
					throw "Invalid credentials";
				} else if (resp.status === 400) {
					throw "Invalid email or password format";
				}
				const data = await resp.json();

				// save your token in the localStorage
				//also you should set your user into the store using the setStore function
				localStorage.setItem("jwt-token", data.token);
				console.log("this came from backend:" , data)
				return data;
			}
		}
	};
};

export default getState;
