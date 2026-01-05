import React from 'react';

const DensityIndicator = ({ density, count }) => {
    let color = 'bg-gray-400';
    let text = 'Unknown';

    if (density === 'Low') {
        color = 'bg-green-500';
        text = 'Low Density';
    } else if (density === 'Medium') {
        color = 'bg-orange-500';
        text = 'Medium Density';
    } else if (density === 'High') {
        color = 'bg-red-600';
        text = 'High Density';
    }

    return (
        <div className="flex flex-col items-center justify-center p-6 bg-white rounded-xl shadow-lg border border-gray-100">
            <div className={`w-24 h-24 rounded-full flex items-center justify-center mb-4 ${color} text-white text-3xl font-bold shadow-inner transition-colors duration-500`}>
                {count !== null ? count : '-'}
            </div>
            <h2 className="text-2xl font-bold text-gray-800 mb-1">{text}</h2>
            <p className="text-gray-500 text-sm">Estimated People Count</p>
        </div>
    );
};

export default DensityIndicator;
