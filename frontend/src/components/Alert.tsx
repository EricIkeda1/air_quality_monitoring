import React, { useEffect, useState } from 'react';
import api from '../services/api';

const Alert: React.FC = () => {
  const [alertas, setAlertas] = useState<{ [key: string]: number }>({});

  useEffect(() => {
    const fetchAlertas = async () => {
      const response = await api.get('/alertas');
      setAlertas(response.data);
    };
    fetchAlertas();
  }, []);

  return (
    <div>
      <h2>Alertas de Qualidade do Ar</h2>
      {Object.keys(alertas).length > 0 ? (
        <ul>
          {Object.entries(alertas).map(([poluente, valor]) => (
            <li key={poluente}>
              {poluente}: {valor}
            </li>
          ))}
        </ul>
      ) : (
        <p>Não há alertas no momento.</p>
      )}
    </div>
  );
};

export default Alert;
