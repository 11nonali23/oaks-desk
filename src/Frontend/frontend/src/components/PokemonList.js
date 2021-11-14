import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Navbar from './Navbar';

export default function PokemonList() {
    const [pokemonList, setpokemonList] = useState([{}])

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/get-all-pokemons')
        .then(response => {
            setpokemonList(response.data)
        })
    }, [])
    
    return (
        <div>
          <header className="PokemonList-header">
              <Navbar />
          </header>
            <div className=" border-2">
                <h1 className="flex-auto text-xl font-medium">Lista di Pokemon</h1>
            </div>
            <div>
                {
                    pokemonList.map( pokemon => {
                        return (
                            <div key={pokemon.id}>
                                <Link className="flex-auto text-s"
                                    to={`/pokemon/${pokemon.id}`}
                                >
                                    { pokemon.name }
                                </Link>
                                <br/>
                            </div>
                        )
                    })
                }
            </div>
        </div>
      );
}