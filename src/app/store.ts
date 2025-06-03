// src/app/store.ts
import { configureStore } from '@reduxjs/toolkit';
import filtersReducer from '../features/filters/filterSlice';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage'; // defaults to localStorage

const persistConfig = {
  key: 'root',
  storage,
};

const persistedReducer = persistReducer(persistConfig, filtersReducer);

export const store = configureStore({
  reducer: {
    filters: persistedReducer,
  },
});

export const persistor = persistStore(store);