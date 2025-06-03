import { Service } from '../types';

// Mock fallback data
const MOCK_SERVICES: Service[] = [
  {
    id: 1,
    title: 'Массаж',
    description: 'Релакс массаж спины',
    price: 2000,
    date: '2025-04-01',
    imageUrl: ''
  },
  {
    id: 2,
    title: 'Спа',
    description: 'Спа-процедуры для лица',
    price: 4500,
    date: '2025-04-05',
    imageUrl: 'https://picsum.photos/id/1018/300/200' 
  }
];

export const fetchServices = async (
  name: string = '',
  minPrice: number = 0,
  maxPrice: number = Infinity,
  fromDate: string = '',
  toDate: string = ''
): Promise<Service[]> => {
  try {
    const params = new URLSearchParams();
    if (name) params.append('name', name);
    if (minPrice) params.append('minPrice', minPrice.toString());
    if (maxPrice < Infinity) params.append('maxPrice', maxPrice.toString());
    if (fromDate) params.append('fromDate', fromDate);
    if (toDate) params.append('toDate', toDate);

    const response = await fetch(`/api/services?${params}`);
    if (!response.ok) throw new Error('Ошибка загрузки услуг');
    return await response.json();
  } catch (error) {
    console.warn('Using mock data due to error:', error);

   
    return MOCK_SERVICES.filter(service => {
      const matchesName = name === '' || service.title.toLowerCase().includes(name.toLowerCase());
      const matchesMinPrice = service.price >= minPrice;
      const matchesMaxPrice = service.price <= maxPrice;
      const matchesFromDate = !fromDate || new Date(service.date) >= new Date(fromDate);
      const matchesToDate = !toDate || new Date(service.date) <= new Date(toDate);

      return matchesName && matchesMinPrice && matchesMaxPrice && matchesFromDate && matchesToDate;
    });
  }
};

