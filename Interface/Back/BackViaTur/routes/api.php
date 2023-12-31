<?php

use App\Http\Controllers\ItensController;
use App\Http\Controllers\SupplierManagerController;
use App\Http\Controllers\UserManagerController;
use Illuminate\Support\Facades\Route;

Route::prefix('supplier')->group(function (){
   Route::get('', [SupplierManagerController::class, 'index']);
   Route::post('',[SupplierManagerController::class, 'store']);
   Route::put('/{id}', [SupplierManagerController::class, 'update']);
   Route::delete('/{id}',[SupplierManagerController::class, 'delete']);
});

Route::prefix('userCreate')->group(function (){
    Route::get('', [UserManagerController::class, 'index']);
    Route::post('',[UserManagerController::class, 'store']);
});

Route::prefix('service')->group(function (){
    Route::get('',[ItensController::class, 'index']);
    Route::post('',[ItensController::class, 'store']);
});
