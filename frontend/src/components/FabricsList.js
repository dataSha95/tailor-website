import React, { useEffect, useState } from 'react';
import api from '../api';

function FabricsList() {
    const [fabrics, setFabrics] = useState([]);

    useEffect(() => {
        // Fetch fabrics from the Django API
        api.get('/fabrics/')
            .then(response => setFabrics(response.data))
            .catch(error => console.error('Error fetching fabrics:', error));
    }, []);

    return (
        <div>
            <h2>Fabrics List</h2>
            <ul>
                {fabrics.map(fabric => (
                    <li key={fabric.id}>
                        {fabric.name} - {fabric.color} - ${fabric.price_per_meter}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default FabricsList;
